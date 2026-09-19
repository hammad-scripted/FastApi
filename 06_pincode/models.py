from fastapi import BaseModel,field_validator


class PinCodeRequest(BaseModel):
    pincode: str
    #pincode must be exactly 6 digits
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6:
            raise ValueError("Pincode must be exactly 6 digits")
        return value    
    
class LocationResponse(BaseModel):
    pincode:str
    city:str
    state:str
    district:str
    
    
class BulkRequest(BaseModel):
    pincodes: list[str]
    
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,values):
        print(values)
        if len(values)==0:
            raise ValueError("Pincodes cannot be empty, please provide at least one pincode")
        if len(values)>10:
            raise ValueError("Pincodes cannot be more than 10, please provide less than 10 pincode")    
        
        for code in values:
            if len(code) != 6:
                raise ValueError("Pincode must be exactly 6 digits")
        
        return values


class BulkResponse(BaseModel):
    status:str="success"
    found:int
    not_found:int
    locations: list[LocationResponse]
    missing:list[str]