
## Authors

- [@ismail-nbiba](https://www.github.com/ismail-nbiba)
- [@med-nbiba](https://www.github.com/med-nbiba)

PROJET SOA : Documentation API REST
## API Reference

#### Get all items

```http
  POST /submit
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **the name of the person submitting the certificate  |
| `id` | `integer` | ** the id of the person submitting the certificate   |
| `date` | `string` | **the date of the certificate |
| `content` | `string` | **the content of the certificate  |

#### Ajouter unité

```http
  GET /data
  Gets the current complaint data.
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. attributes de la class id |

```http
  GET /api/certifs/<id>
  Gets the name, id, and list of items for a given id. The items contain the following data:
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `integer` | ** the id of the person submitting the certificate   |

OUTPUT JSON ===>

certificate id: the id of the certificate (integer)

certificate date: the date of the certificate (string)

isapproved: a boolean value indicating whether the certificate is approved or not


```http
 POST /api/certifs
 Adds a new item with the following data:
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `null` | `null` | **null |
