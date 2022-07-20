
import os 
import json
import requests

from errbot import BotPlugin, botcmd, Message, arg_botcmd, re_botcmd


class Vdsworker(BotPlugin):  

#Account
   
    @botcmd  
    def account(self, msg, base ):  
        return self.__account(msg, ) 
    @staticmethod 
    def __account(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/account',                        
                                        headers=newHeaders)
        json_data = response.json()        
        account_data = (json.dumps(json_data, indent=4))    
        return(account_data) 

#Servers 

    @botcmd  
    def servers(self, msg, base ):  
        return self.__servers(msg, ) 
    @staticmethod 
    def __servers(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/scalets',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     


#Background
 
    @botcmd  
    def locations(self, msg, base ):  
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
    def images(self, msg, base ):  
        return self.__images(msg, ) 
    @staticmethod 
    def __images(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/images',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)    

#Configurations

    @botcmd  
    def rplans(self, msg, base ):  
        return self.__rplans(msg, ) 
    @staticmethod 
    def __rplans(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/rplans',                        
                                        headers=newHeaders)
        json_data = response.json()        
        account_data = (json.dumps(json_data, indent=4))    
        return(account_data) 

    @botcmd  
    def prices(self, msg, base ):  
        return self.__prices(msg, ) 
    @staticmethod 
    def __prices(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/prices',                        
                                        headers=newHeaders)
        json_data = response.json()        
        account_data = (json.dumps(json_data, indent=4))    
        return(account_data) 

#SSHkeys

    @botcmd  
    def sshkeys(self, msg, base ):  
        return self.__sshkeys(msg, ) 
    @staticmethod 
    def __sshkeys(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/sshkeys',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)          
    

    @arg_botcmd("key_p1", type=str) 
    @arg_botcmd("key_p2", type=str) 
    @arg_botcmd("key_p3", type=str) 
    @arg_botcmd("key_p4", type=str) 
    
    def sshkey(self, msg, key_p1, key_p2, key_p3, key_p4 ):  
        return self.__sshkey(msg, key_p1, key_p2, key_p3, key_p4 ) 
    @staticmethod 
    def __sshkey(msg,key_p1, key_p2, key_p3, key_p4  ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN"),
                    'Content-Type': 'application/json;charset=UTF-8'}
        key = key_p4+" "+key_p3+" "+key_p2
        newData = {"key": key,"name": key_p1 }                     
        response = requests.post('https://api.vscale.io/v1/sshkeys',                        
                                        headers=newHeaders,
                                        json=newData )  
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)                                          
                                     
    
    
    @arg_botcmd("key_id", type=str) 
    def delete_sshkey(self, msg, key_id ):  
        return self.__delete_sshkey(msg, key_id ) 
    @staticmethod 
    def __delete_sshkey(msg, key_id ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN"),
                    'Content-Type': 'application/json;charset=UTF-8'}
        response = requests.delete(f'https://api.vscale.io/v1/sshkeys/{key_id}',                        
                                        headers=newHeaders)
        if response.status_code != 204:                                
            json_data = response.json()        
            data = (json.dumps(json_data, indent=4))    
            return(data)         
        else:
            return(f'key with id {key_id} deleted' )


#Billing

    @botcmd  
    def balance(self, msg, base ):  
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
    def payments(self, msg, base ):  
        return self.__payments(msg, ) 
    @staticmethod 
    def __payments(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/payments',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)     
        
    @botcmd  
    def consumption(self, msg, base ):  
        return self.__consumption(msg, ) 
    @staticmethod 
    def __consumption(msg, ):
        newHeaders = {'X-Token': os.getenv("VDS_TOKEN")}
        response = requests.get('https://api.vscale.io/v1/billing/consumption?start=&end=',                        
                                        headers=newHeaders)
        json_data = response.json()        
        data = (json.dumps(json_data, indent=4))    
        return(data)      