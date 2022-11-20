from cgitb import text
from typing import Dict
import pandas as pd

import uvicorn

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests


from src.random_forest.rf_model import Rf_Model, rf_get_model

app = FastAPI()

origins = ['*']


app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)











class EngagementRequest(BaseModel):
    dct : dict


class EngagementResponse(BaseModel):
    engagement: int


@app.post("/predict_engagement", response_model=EngagementResponse)
def predict(request: EngagementRequest, model: Rf_Model = Depends(rf_get_model)):
    categorical_features = []
    columns_to_encode = ['Age_Group','Gender','Countries','Marital','provider','esp']

    
    df_final_columns = ['Date',
                        'Template',
                        'Age_Group.70+',
                        'Age_Group.[18, 30)',
                        'Age_Group.[30, 40)',
                        'Age_Group.[40, 50)',
                        'Age_Group.[50, 60)',
                        'Age_Group.[60, 70)',
                        'Gender.F',
                        'Gender.M',
                        'Countries.Belgium',
                        'Countries.France',
                        'Countries.Germany',
                        'Countries.Italy',
                        'Countries.Netherlands',
                        'Countries.Portugal',
                        'Countries.Spain',
                        'Countries.United Kingdom',
                        'Marital.divorced',
                        'Marital.married',
                        'Marital.single',
                        'Marital.unknown',
                        'provider.prv-11',
                        'provider.prv-13',
                        'provider.prv-19',
                        'provider.prv-21',
                        'provider.prv-22',
                        'provider.prv-37',
                        'provider.prv-5',
                        'esp.Aol',
                        'esp.Gmail',
                        'esp.Icloud',
                        'esp.Outlook',
                        'esp.Yahoo',
                        'Conversion']

    df_final = pd.DataFrame(columns=df_final_columns)

    dt = pd.DataFrame(request.dct, index=[0])

    for col in columns_to_encode:
        encoded_df = pd.get_dummies(dt[col])
        encoded_df.columns = [col.replace(' ', '.') + '.' + x for x in encoded_df.columns]
        
        categorical_features += list(encoded_df.columns)
        
        dt = pd.concat([dt, encoded_df], axis=1)
    
    dt = dt.reindex(labels = df_final.columns, axis = 1, fill_value = 0).drop(columns = ['Conversion'])

    engagement = int(Rf_Model.predict(dt))
    return EngagementResponse(
        engagement=engagement
    )

