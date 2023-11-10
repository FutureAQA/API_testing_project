from tests.test_kate.generator.generator import generated_person


def update_user_data(person_info):
    update_person_info = next(generated_person())
    update_person_info['id'] = person_info['id']
    update_person_info['username'] = person_info['username']
    return update_person_info



