import json
from fastapi import APIRouter, Depends, status, Request, HTTPException
from funds.schemas import MutualFundOptions
from funds.services import fetch_fund_schemes
from funds.schemas import FundSchemaList, SchemeNumber
from fastapi.responses import Response
from auth.utils import decode_access_token

router = APIRouter()

async def authentication_middleware(request: Request):
    auth_token = request.headers.get('authorization')
    if not auth_token:
        raise HTTPException(status_code=400, detail="Authorisation token missing.")
    auth_token = auth_token.replace("Bearer ", "")
    decode_access_token(auth_token)

@router.get("/fund-families/", dependencies=[Depends(authentication_middleware)])
async def get_fund_families():
    return MutualFundOptions

@router.get("/family-schemes/", dependencies=[Depends(authentication_middleware)])
async def get_family_schemes(fund_name: str, response_model=FundSchemaList):
    fund_name = fund_name.strip()
    if fund_name not in MutualFundOptions:
        return Response(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=json.dumps({
            "message": "Invalid family fund name provided."
        })
    )
    schemes = fetch_fund_schemes(fund_name)
    return schemes

@router.post("/family-schemes/buy/", dependencies=[Depends(authentication_middleware)])
async def buy_family_schemes(scheme_number: SchemeNumber):
    '''Logic to buy a scheme'''
    return {"message": "Order created succesfully"}

