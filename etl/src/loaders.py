import pandas as pd
import itertools
from typing import List, Dict, Any
from pydantic import ValidationError
from models import ApartmentData

def loadAptData(apts) -> pd.DataFrame:
    aptsList = list(itertools.chain.from_iterable(apts))

    validated_property_objects: List[ApartmentData] = []
    validation_errors_list: List[Dict[str, Any]] = []

    print("Starting conversion of dictionaries to Pydantic objects...")
    for index, record_dict in enumerate(aptsList):
        try:
            # This is where Pydantic does its magic:
            # - Validates data types
            # - Coerces types where possible (e.g., string "320000" to int 320000)
            # - Checks for required fields (if any are not Optional)
            # - Applies default values (if defined in your Pydantic model)
            property_obj = ApartmentData(**record_dict)
            validated_property_objects.append(property_obj)
        except ValidationError as e:
            # Handle the validation error
            # You can log it, store it, or decide to skip the record
            print(f"--- Validation Error for record at index {index} ---")
            print(f"Original Dictionary: {record_dict}")
            print(f"Pydantic Errors:\n{e.errors()}\n") # .errors() gives a structured list of errors
            validation_errors_list.append({
                "index": index,
                "original_data": record_dict,
                "errors": e.errors() # Get detailed error information
            })
        except Exception as ex: # Catch any other unexpected errors during instantiation
            print(f"--- Unexpected Error for record at index {index} ---")
            print(f"Original Dictionary: {record_dict}")
            print(f"Error: {ex}\n")
            validation_errors_list.append({
                "index": index,
                "original_data": record_dict,
                "errors": str(ex)
            })
    
    
    print(f"\nSuccessfully validated and converted {len(validated_property_objects)} records into Pydantic objects.")
    if validation_errors_list:
        print(f"Encountered {len(validation_errors_list)} records with validation/conversion errors.")    
    
    # Convert the list of Pydantic objects into a Pandas DataFrame ---
    if validated_property_objects:
        df = pd.DataFrame([obj.model_dump() for obj in validated_property_objects])

        print("\n--- DataFrame created successfully ---")
        print(df.head())
        print("\nDataFrame Info:")
        df.info()
    else:
        print("\nNo valid data to create a DataFrame.")

    return df