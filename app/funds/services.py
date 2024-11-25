import requests
from typing import List, Optional
from funds.schemas import FundSchemaList
from conf.configuration import get_settings

settings = get_settings()


def fetch_fund_schemes(fund_name: str) -> Optional[FundSchemaList]:
    url = settings.RAPID_API_URL

    params = {
        "Scheme_Type": "Open",
        "Mutual_Fund_Family": fund_name
    }
    headers = {
      'x-rapidapi-host': settings.RAPID_API_HOST,
      'x-rapidapi-key': settings.RAPID_API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        schemes = response.json()
        return FundSchemaList(options=schemes)
    
