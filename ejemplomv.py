
import datetime

def retrieve_age_eafp(person_dict):
  
  try:
    birth_year = person_dict['birth']
    current_year = datetime.date.today().year
    return current_year - birth_year
  except KeyError:
    return None
  except (TypeError, ValueError):
    return None

def retrieve_age_lbyl(person_dict):
  if 'birth' in person_dict and isinstance(person_dict['birth'], int):
    birth_year = person_dict['birth']
    current_year = datetime.date.today().year
    return current_year - birth_year
  else:
    return None

# Example dictionaries
person1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
person2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
person3 = {'name': 'Peter', 'last_name': 'Jones', 'birth': 'unknown'} # Example with invalid birth year type

print(f"Age of person1 (EAFP): {retrieve_age_eafp(person1)}")
print(f"Age of person1 (LBYL): {retrieve_age_lbyl(person1)}")
print(f"Age of person2 (EAFP): {retrieve_age_eafp(person2)}")
print(f"Age of person2 (LBYL): {retrieve_age_lbyl(person2)}")
print(f"Age of person3 (EAFP): {retrieve_age_eafp(person3)}")
print(f"Age of person3 (LBYL): {retrieve_age_lbyl(person3)}")