EXEMPLE_REQUEST={
	"name":"Usuario Teste",
	"email":"usuario@hotmail.com",
	"username":"usuario",
	"password":"senha1233",
	"scopes":"user:create"
}


EXEMPLE_RESPONSE={
    201:{
        "description":"Successful Create",
        "content":{
            "id": 13,
            "username": "usuario",
            "scopes": "user:create"
        }
    }
}