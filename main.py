from fastapi import FastAPI, HTTPException

app = FastAPI()

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]

@app.get("/shoes")
def get_all_shoes(manufacturer: str = None):
    if manufacturer is not None:
        return [shoe for shoe in shoes if shoe["manufacturer"].lower() == manufacturer.lower()]
    return shoes

@app.get("/shoes/{shoe_id}")
def get_shoe_by_id(shoe_id: int):
    shoe = next((shoe for shoe in shoes if shoe["id"] == shoe_id), None)
    if shoe is None:
        raise HTTPException(status_code=404, detail="Shoe not found")