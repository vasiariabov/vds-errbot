
import os 
import json
import requests

from errbot import BotPlugin, botcmd, Message, arg_botcmd, re_botcmd


class Vdsworker(BotPlugin):  
   
    @botcmd  
    def bot_account(self, msg, base ):  
        return self.__account(msg, ) 
    @staticmethod 
    def __account(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/account',                        
                                        headers=newHeaders)
        json_data = response.json()        
        account_data = (json.dumps(json_data, indent=4))    
        return(account_data) 
    
    @botcmd  
    def bot_servers(self, msg, base ):  
        return self.__servers(msg, ) 
    @staticmethod 
    def __servers(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/scalets',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     

    @botcmd  
    def bot_locations(self, msg, base ):  
        return self.__locations(msg, ) 
    @staticmethod 
    def __locations(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/locations',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)          

    @botcmd  
    def bot_images(self, msg, base ):  
        return self.__images(msg, ) 
    @staticmethod 
    def __images(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/images',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     

    @botcmd  
    def bot_balance(self, msg, base ):  
        return self.__balance(msg, ) 
    @staticmethod 
    def __balance(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/balance',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     
        
    @botcmd  
    def bot_sshkeys(self, msg, base ):  
        return self.__sshkeys(msg, ) 
    @staticmethod 
    def __sshkeys(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/sshkeys',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)          
    
    @botcmd  
    def bot_locations(self, msg, base ):  
        return self.__locations(msg, ) 
    @staticmethod 
    def __locations(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/locations',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)         