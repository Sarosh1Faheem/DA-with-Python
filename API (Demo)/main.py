from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# --------------------------------------------------
# 1. CREATE THE API APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="My DEMO API",
    description="Hello, This is Muhammad Sarosh Faheem. This is my first API i've Created for learning purposes, demonstrating CRUD operations",
    version="1.0.0"
)


# --------------------------------------------------
# 2. DEFINE THE MATERIAL DATA MODEL
# --------------------------------------------------

class Material(BaseModel):
    material_name: str = Field(min_length=2, max_length=100)
    category: str = Field(min_length=2, max_length=50)
    stock: int = Field(ge=0)
    price: float = Field(gt=0)


# --------------------------------------------------
# 3. TEMPORARY DATABASE
# --------------------------------------------------

# In-memory storage: data will disappear when the
# application restarts.

materials = {
    1001: {
        "material_name": "Laptop",
        "category": "Electronics",
        "stock": 50,
        "price": 75000.0
    },
    1002: {
        "material_name": "Keyboard",
        "category": "Accessories",
        "stock": 100,
        "price": 2500.0
    }
}

# Generate material IDs automatically.
next_material_id = 1003


# --------------------------------------------------
# 4. ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to the Materials Management API",
        "documentation": "/docs"
    }


# --------------------------------------------------
# 5. READ ALL MATERIALS - GET
# --------------------------------------------------

@app.get("/materials")
def get_all_materials():
    return {
        "count": len(materials),
        "materials": [
            {"material_id": material_id, **material}
            for material_id, material in materials.items()
        ]
    }


# --------------------------------------------------
# 6. READ ONE MATERIAL - GET
# --------------------------------------------------

@app.get("/materials/{material_id}")
def get_material(material_id: int):

    if material_id not in materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )

    return {
        "material_id": material_id,
        **materials[material_id]
    }


# --------------------------------------------------
# 7. CREATE A MATERIAL - POST
# --------------------------------------------------

@app.post(
    "/materials",
    status_code=status.HTTP_201_CREATED
)
def create_material(material: Material):

    global next_material_id

    material_id = next_material_id
    next_material_id += 1

    materials[material_id] = material.model_dump()

    return {
        "message": "Material created successfully",
        "material_id": material_id,
        **materials[material_id]
    }


# --------------------------------------------------
# 8. UPDATE A COMPLETE MATERIAL - PUT
# --------------------------------------------------

@app.put("/materials/{material_id}")
def update_material(material_id: int, material: Material):

    if material_id not in materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )

    materials[material_id] = material.model_dump()

    return {
        "message": "Material updated successfully",
        "material_id": material_id,
        **materials[material_id]
    }


# --------------------------------------------------
# 9. UPDATE SELECTED FIELDS - PATCH
# --------------------------------------------------

@app.patch("/materials/{material_id}")
def partially_update_material(
    material_id: int,
    updates: dict
):

    if material_id not in materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )

    allowed_fields = {
        "material_name",
        "category",
        "stock",
        "price"
    }

    invalid_fields = set(updates.keys()) - allowed_fields

    if invalid_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=f"Invalid fields: {sorted(invalid_fields)}"
        )

    # Combine existing data with the requested changes.
    updated_data = {
        **materials[material_id],
        **updates
    }

    # Validate the complete updated material.
    try:
        validated_material = Material(**updated_data)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Invalid material data"
        ) from exc

    materials[material_id] = validated_material.model_dump()

    return {
        "message": "Material partially updated successfully",
        "material_id": material_id,
        **materials[material_id]
    }


# --------------------------------------------------
# 10. DELETE A MATERIAL - DELETE
# --------------------------------------------------

@app.delete("/materials/{material_id}")
def delete_material(material_id: int):

    if material_id not in materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )

    deleted_material = materials.pop(material_id)

    return {
        "message": "Material deleted successfully",
        "material_id": material_id,
        "deleted_material": deleted_material
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)