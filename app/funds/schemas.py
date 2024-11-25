from pydantic import BaseModel
from typing import List
from enum import Enum

class MutualFundEnum(str, Enum):
    MF_360_ONE = '360 ONE Mutual Fund (Formerly Known as IIFL Mutual Fund)'
    ADITYA_BIRLA = 'Aditya Birla Sun Life Mutual Fund'
    AXIS = 'Axis Mutual Fund'
    BAJAJ_FINSERV = 'Bajaj Finserv Mutual Fund'
    BANDHAN = 'Bandhan Mutual Fund'
    BANK_OF_INDIA = 'Bank of India Mutual Fund'
    BARODA_BNP_PARIBAS = 'Baroda BNP Paribas Mutual Fund'
    CANARA_ROBECO = 'Canara Robeco Mutual Fund'
    DSP = 'DSP Mutual Fund'
    EDELWEISS = 'Edelweiss Mutual Fund'
    FRANKLIN_TEMPLETON = 'Franklin Templeton Mutual Fund'
    GROWW = 'Groww Mutual Fund'
    HDFC = 'HDFC Mutual Fund'
    HSBC = 'HSBC Mutual Fund'
    HELIOS = 'Helios Mutual Fund'
    ICICI_PRUDENTIAL = 'ICICI Prudential Mutual Fund'
    ITI = 'ITI Mutual Fund'
    INVESCO = 'Invesco Mutual Fund'
    JM_FINANCIAL = 'JM Financial Mutual Fund'
    KOTAK_MAHINDRA = 'Kotak Mahindra Mutual Fund'
    LIC = 'LIC Mutual Fund'
    MAHINDRA_MANULIFE = 'Mahindra Manulife Mutual Fund'
    MIRAE_ASSET = 'Mirae Asset Mutual Fund'
    MOTILAL_OSWAL = 'Motilal Oswal Mutual Fund'
    NJ = 'NJ Mutual Fund'
    NAVI = 'Navi Mutual Fund'
    NIPPON_INDIA = 'Nippon India Mutual Fund'
    OLD_BRIDGE = 'Old Bridge Mutual Fund'
    PGIM_INDIA = 'PGIM India Mutual Fund'
    PPFAS = 'PPFAS Mutual Fund'
    QUANTUM = 'Quantum Mutual Fund'
    SBI = 'SBI Mutual Fund'
    SAMCO = 'Samco Mutual Fund'
    SHRIRAM = 'Shriram Mutual Fund'
    SUNDARAM = 'Sundaram Mutual Fund'
    TATA = 'Tata Mutual Fund'
    TAURUS = 'Taurus Mutual Fund'
    TRUST = 'Trust Mutual Fund'
    UTI = 'UTI Mutual Fund'
    UNION = 'Union Mutual Fund'
    WHITEOAK_CAPITAL = 'WhiteOak Capital Mutual Fund'
    ZERODHA = 'Zerodha Mutual Fund'
    QUANT = 'quant Mutual Fund'

MutualFundOptions = [member.value for member in MutualFundEnum]

class FundScheme(BaseModel):
    Scheme_Code: int
    ISIN_Div_Payout_ISIN_Growth: str
    ISIN_Div_Reinvestment: str
    Scheme_Name: str
    Net_Asset_Value: float
    Date: str  
    Scheme_Type: str
    Scheme_Category: str
    Mutual_Fund_Family: str

class FundSchemaList(BaseModel):
    options: List[FundScheme]

class SchemeNumber(BaseModel):
    number: int