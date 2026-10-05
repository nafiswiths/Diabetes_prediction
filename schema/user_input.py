from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator 
from typing import Literal, Annotated
import pickle
import pandas as pd
#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	

class UserInput(BaseModel):
    Pregnancies: Annotated[int, Field(ge=0, le=20, description="Number of times pregnant")]
    Glucose: Annotated[int, Field(ge=0, le=200, description="Plasma glucose concentration a 2 hours in an oral glucose tolerance test")]
    BloodPressure: Annotated[int, Field(ge=0, le=140, description="Diastolic blood pressure (mm Hg)")]
    SkinThickness: Annotated[int, Field(ge=0, le=100, description="Triceps skin fold thickness (mm)")]
    Insulin: Annotated[int, Field(ge=0, le=900, description="2-Hour serum insulin (mu U/ml)")]
    BMI: Annotated[float, Field(ge=0.0, le=70.0, description="Body mass index (weight in kg/(height in m)^2)")]
    DiabetesPedigreeFunction: Annotated[float, Field(ge=0.0, le=2.5, description="Diabetes pedigree function")]
    Age: Annotated[int, Field(ge=10, le=100, description="Age (years)")]