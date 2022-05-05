<div align="center"><h1>MOBAPI</h1></div>

O objetivo do **MOBAPI** é fornecer uma plataforma para que jogadores de MOBAs (Multiplayer Online Battle Arena) possam se encontrar e formar times.

A API é extensível e pode ser utilizada para qualquer MOBA, bem como adaptada para atender a jogos de outros gêneros como First-Person Shooter Games.

# Generic Error Message

**URL** : any endpoint

**Method** : any

## Error Response

**Condtition** : Request on a route/endpoint that does noe exist.

**Code** : `404 NOT FOUND`

**Content** :

```json
{
	"err": "Route not found"
}

```

# Users Route

## **List Users**

Show all user accounts registered on `game`.

**URL** : `/:game/users/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Response

**Condition** : User can see one or more accounts.

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

Create an user account if an the username does not already exist.

**URL** : `/:game/users/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** :

Provide name, email. password and a bio to create an user account.
Bio is optional.

```json
{
	"name": "[20 chars max]",
	"email": "[50 chars max, unique]",
	"bio": "[text]",
	"password": "[text]
}
```

**Data example** Bio is optional.

```json
{
	"name": "name",
	"email": "email",
	"bio": "your bio",
	"password": "1234"
}
```

## Success Response

**Condition** : If everything is OK and the email does not already exists.

**Code** : `201 CREATED`

**Content example**

```json
adicionar exemplo aqui

```

## Error Responses

**Condition** : If email already exists.

**Code** : 

**Content** :
```json
adicionar exemplo aqui
```

## Or

**Condition** : If fields are missed.

**Code** : `400 BAD REQUEST`

**Content**

```json
adicionar exemplo aqui
```
