# Bank and Branch API

This is a simple Django-based API that provides information about banks and their branches.

![Bank and Branch API](images/sample-image.png)

---

## Features

- Fetch a list of all banks.
- Retrieve branch details using an IFSC code.

---

## Endpoints

### 1. List All Banks
**URL:** `/banks/`  
**Method:** `GET`  
**Response Example:**
```json
[
    {
        "id": 1,
        "name": "STATE BANK OF INDIA"
    },
    {
        "id": 2,
        "name": "PUNJAB NATIONAL BANK"
    }
]
```

### 2. Get Branch Details by IFSC
**URL:** `/branches/<ifsc>/`  
**Method:** `GET`  
**Response Example:**
```json
{
    "ifsc": "ABHY0065004",
    "bank": {
        "id": 60,
        "name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    },
    "branch": "BHANDUP",
    "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
    "city": "MUMBAI",
    "district": "GREATER MUMBAI",
    "state": "MAHARASHTRA"
}
```

---

## Notes

- Ensure the database is populated by running the provided scripts.
- Use tools like `Postman` or `curl` to test the API.

---
