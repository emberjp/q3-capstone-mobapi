<div align="center"><h1>MOBAPI</h1></div>

O objetivo do **MOBAPI** é fornecer uma plataforma para que jogadores de MOBAs (Multiplayer Online Battle Arena) possam se encontrar e formar times.

A API é extensível e pode ser utilizada para qualquer MOBA, bem como adaptada para atender a jogos de outros gêneros como First-Person Shooter Games.

**MOBAPI** é acessada pelo site https://q3-capstone-mobapi.herokuapp.com/

# Generic Error Messages

**URL** : any endpoint

**Method** : any

## Error Responses

**Condtition** : Request on a route/endpoint that does not exist.

**Request example** : `/lol/accounts`

**Code** : `404 NOT FOUND`

**Content** :

```json
{
	"err": "Route not found"
}
```

## Or

**Condtition** : Request on a game that does not exist.

**Request example** : `/dota/users`

**Code** : `404 NOT FOUND`

**Content** :

```json
{
	"err": "Game dota not found"
}
```

# Users Route

## **Login**

Used to collect a token for a registered user.

**URL** : `/login/`

**Method** : `POST`

**Auth required** : No

**Data constraints**

```json
{
    "email": "[valid email address]",
    "password": "[password]"
}
```

**Data example**

```json
{
    "email": "john@email.com",
    "password": "doe1234"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
	"access_token": "[token]"
}
```

## Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
	"msg": "Missing Authorization Header"
}
```

## **List Users**

Show all user accounts registered on `game` and filtered by `position`

**URL** : `/:game/users?position=[position]`

**Method** : `GET`

**Auth required** : Yes

**Permissions required** : None

**Data constraints** : `{}`

## Success Response

**Condition** : User can see one or more accounts.

**Request example** : `/lol/users`

**Code** : `200 OK`

**Content** :

```json
[
	{
		"bio": "your bio",
		"champions": [],
		"email": "email",
		"game": [],
		"id": 1,
		"name": "name",
		"positions": [],
		"teams": []
	},
	{
		"bio": "your bio",
		"champions": [],
		"email": "email2",
		"game": [],
		"id": 10,
		"name": "names",
		"positions": [],
		"teams": []
	}
]
```

## Error Response

**Condition** : no users registered.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
	"err": "Nothing to list"
}
```

## **Create User**

Create an user account on `game` if an username does not already exist.

**URL** : `/:game/users/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints** : Provide name, email, password and a bio to create an user account.
Bio is optional.

```json
{
	"name": "[20 chars max]",
	"email": "[50 chars max, unique]",
	"bio": "[text]",
	"password": "[text]"
}
```

**Request example** : `/lol/users`

**Data example** : Bio is optional.

```json
{
	"name": "name",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

## Success Response

**Condition** : Everything is OK and the email does not already exists.

**Code** : `201 CREATED`

**Content example** :

```json
{
	"bio": "your bio",
	"email": "email",
	"id": 1,
	"name": "name"
}

```

## Error Responses

**Condition** : Email already exists.

**Code** : `409 CONFLICT`

**Content** :

```json
{
	"err": "this email is already in use"
}
```

## Or

**Condition** : Fields have an invalid length.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
	"name": "This_is_definitely_a_very_big_name",
	"email": "email3",
	"bio": "your bio",
	"password": "1234"
}
```

## **Edit User**

Edit informations from an existing user, given its `id`.

**URL** : `/:game/users/:id`

**Method** : `POST`

**Auth required** : Yes

**Permissions required** : None

**Data constraints** : Provide name, email, password and/or a bio to edit an user account.

```json
{
	"name": "[20 chars max]",
	"email": "[50 chars max, unique]",
	"bio": "[text]",
	"password": "[text]"
}
```

**Request example** : `/lol/users`

**Data example** :

```json
{
	"name": "name",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

## Success Response

**Condition** : Everything is OK.

**Data example** :

```json
{
	"name": "Test",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

**Code** : `201 CREATED`

**Content example** :

```json
{
	"bio": "your bio",
	"champions": [],
	"email": "email",
	"game": [],
	"id": 1,
	"name": "Test",
	"positions": [],
	"teams": []
}
```

## Error Response

**Condition** : Fields have an invalid length

**Data example** :

```json
{
	"name": "This_is_a_really_big_name",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

**Code** : `409 CONFLICT`

**Content** :
```json
{
	"err": "Name or email value is too large: name must be a maximum of 20 characters and email must be 50 characters"
}
```

## **Delete User**

Delete an existing user, given its `id`.

**URL** : `/:game/users/:id`

**Method** : `DELETE`

**Auth required** : Yes

**Permissions required** : None

**Data constraints** : `{}`

**Request example** : `/lol/users/1`

## Success Response

**Condition** : If everything is OK and `id` exists.

**Code** : `204 NO CONTENT`

**Content example**

```json

```

## Error Response

**Condition** : `id` does not exist

**Code** : 

**Content** :
```json
{
	"err": "id 2 does not exist"
}
```
# Champions Route

## **List Champions**

Show all champions registered on `game`.

**URL** : `/:game/champions`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Response

**Condition** : User can see one or more champions.

**Request example** : `/lol/champions`

**Code** : `200 OK`

**Content** :

```json
[
	{
		"id": 1,
		"img_url": "placeholder",
		"info": "placeholder",
		"name": "Ahri",
		"roles": [
			{
				"id": 3,
				"name": "mage"
			}
		]
	}
]
```

## Error Response

**Condition** : no champions registered.

**Code** : `404 NOT FOUND`

**Content** :
```json
{
	"err": "Nothing to list"
}
```

## **Create Champion**

Create a champion on `game` if a champion does not already exist.

**URL** : `/:game/champions/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints** : Provide name, picture, info and game to create a champion.

```json
{
	"name": "[16 chars max]",
	"img_url": "[text]",
	"info": "[text]",
	"game": "[text]"
}
```

**Request example** : `/lol/champions`

**Data example** :

```json
{
	"name": "name1",
	"img_url": "img1",
	"info": "link1",
	"game": "game1"
}
```

## Success Response

**Condition** : Everything is OK.

**Code** : `201 CREATED`

**Content example** :

```json
{
    "id": 1,
	"name": "name1",
	"img_url": "img1",
	"info": "link1",
	"game": "game1"
}
```

## **Edit Champion**

Edit informations from an existing champion, given its `id`.

**URL** : `/:game/champions/:id`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints** : Provide name, picture, info and game to edit a champion.

```json
{
	"name": "name1",
	"img_url": "img1",
	"info": "link1",
	"game": "game1"
}
```

**Request example** : `/lol/champions`

**Data example** :

```json
{
	"info": "test"
}
```

## Success Response

**Condition** : Everything is OK.

**Data example** :

```json
{
	"name": "Test",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

**Code** : `200 OK`

**Content example** :

```json
{
	"id": 1,
	"img_url": "placeholder",
	"info": "test",
	"name": "Ahri",
	"roles": [
		{
			"id": 3,
			"name": "mage"
		}
	]
}
```

## Error Response

**Condition** : `id` does not exit

**Code** : `404 NOT FOUND`

**Content** :
```json
{
	"err": "20 doesn't exist"
}
```

## **Delete Champion**

Delete an existing champion, given its `id`.

**URL** : `/:game/champions/:id`

**Method** : `DELETE`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

**Request example** : `/lol/champions/1`

## Success Response

**Condition** : If everything is OK and `id` exists.

**Code** : `204 NO CONTENT`

**Content example**

```json

```

## Error Response

**Condition** : `id` does not exist

**Code** : `404 NOT FOUND`

**Content** :
```json
{
	"err": "id 20 does not exist"
}
```
