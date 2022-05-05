<div align="center"><h1>MOBAPI</h1></div>

O objetivo do **MOBAPI** é fornecer uma plataforma para que jogadores de MOBAs (Multiplayer Online Battle Arena) possam se encontrar e formar times.

A API é extensível e pode ser utilizada para qualquer MOBA, bem como adaptada para atender a jogos de outros gêneros como First-Person Shooter Games.

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

# Login

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
    "email": "iloveauth@example.com",
    "password": "abcd1234"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d"
}
```

## Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "non_field_errors": [
        "Unable to login with provided credentials."
    ]
}
```

# Users Route

## **List Users**

Show all user accounts registered on `game`.

**URL** : `/:game/users`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Response

**Condition** : User can see one or more accounts.

**Request example** : `/lol/users`

**Code** : `200 OK`

**Content** :

```json
adicionar exemplo aqui
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

**Auth required** : NO

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

**Content example**

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

**Code** : 

**Content** :
```json
{
	"err": "this email is already in use"
}
```

## Or

**Condition** : Fields have an invalid length.

**Code** : `400 BAD REQUEST`

**Content**

```json
adicionar exemplo aqui
```

## Or

**Condition** : Fields are missed.

**Code** : `400 BAD REQUEST`

**Content**

```json
adicionar exemplo aqui
```

## **Edit User**

Edit informations from an existing user, given its `id`.

**URL** : `/:game/users/:id`

**Method** : `POST`

**Auth required** : YES

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

**Code** : `201 CREATED`

**Content example**

```json
adicionar exemplo aqui

```

## Error Responses

**Condition** : Fields have an invalid length

**Code** : 

**Content** :
```json
adicionar exemplo aqui
```

## Or

**Condition** : Fields are missed.

**Code** : `400 BAD REQUEST`

**Content**

```json
adicionar exemplo aqui
```

## **Delete User**

Delete an existing user, given its `id`.

**URL** : `/:game/users/:id`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

**Request example** : `/lol/users/1`

## Success Response

**Condition** : If everything is OK and `id` exists.

**Code** :

**Content example**

```json
adicionar exemplo aqui

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
