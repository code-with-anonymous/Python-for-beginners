def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case 400:
            return "Bad Request "
        case _: 
            return "Unknown status"  


print(http_status(400))