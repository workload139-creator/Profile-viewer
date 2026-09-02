import requests as r 
print("github_profile_viewer")
username=input("username:")
url=f"https://api.github.com/users/{username}"
try:
	response=r.get(url,timeout=10)
	
	if response .status_code==200:
	    data=response.json()
	    
	  
        #data=response.json()
	    print("\nprofileview")
	    print("name",data.get("name"))
	    print("username",data.get("login"))
	    print("followers",data.get("followers"))
	    print("following",data.get("following"))            
    	
	    print("locatioan",data.get("location"))
	    print("public_repo",data.get("public_repos"))
	    print("compnay",data.get("company"))
	    print("blog",data.get("blog"))
	    print("profile_url",data.get("html_url"))
	    print("avatar_url",data.get("avatar_url"))
	    print("created",data.get("created_at"))
	    
	elif  response.status_code==404:
    	
		print("user not found")
			
except r.exceptions.RequestException as e:
	print("network error",e)			
	
	
	
	
	
	
	
	
	
	
	
	
	
	