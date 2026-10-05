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
    weight: Annotated[float, Field(..., gt=0, lt=500, description="Weight of the user in kilograms", examples=[90.0])]
    height: Annotated[float, Field(..., gt=0, lt=4, description="Height of the user in meters", examples=[1.65])]
    DiabetesPedigreeFunction: Annotated[float, Field(ge=0.0, le=2.5, description="Diabetes pedigree function")]
    Age: Annotated[int, Field(ge=10, le=100, description="Age (years)")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2),  2)
