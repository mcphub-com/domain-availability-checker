import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/navii/api/domain-availability-checker'

mcp = FastMCP('domain-availability-checker')

@mcp.tool()
def bulkcheck(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Check domain names availability in bulk, with up to 5 domains'''
    url = 'https://domainstatus.p.rapidapi.com/v1/domain/available'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'domainstatus.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def name_and_tld(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Check by Name and TLD separately'''
    url = 'https://domainstatus.p.rapidapi.com/v1/domain/available'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'domainstatus.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def domain_name(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Check by Domain Name (includes TLD)'''
    url = 'https://domainstatus.p.rapidapi.com/v1/domain/available'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'domainstatus.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
