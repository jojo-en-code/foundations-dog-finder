# from website import score_comp
def calculate_range(dog_breed_list, score):
    dog_breed_range_list = []
    for dog_breed in dog_breed_list:
        min_score=dog_breed.min_score
        max_score=dog_breed.max_score
        if score > min_score and score < max_score:
            dog_name=dog_breed.name
            dog_breed_range_list.append(dog_name)

    return dog_breed_range_list