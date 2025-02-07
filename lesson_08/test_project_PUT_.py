import pytest
from YouGileAPI.projects_api import ProjectAPI

project_api = ProjectAPI(
    token='zdxJCD1R3GOMO7Pt3Ncu3Di0rjxiy0bni2Z-es-OwA7fwhr2sBZkGjMNRlR8k8y5'
)


@pytest.mark.run(order=4)
def test_update_project_positive():
    project_api.create_project_with_role('worker', 'f92aabc1-2754-403d-a238-f722107e3595')
    project_api.get_and_check_first_project()
    update_payload = {'title': 'Обновленный проект'}
    project_api.check_update_project(update_payload=update_payload)  # Обновляем проект без явного указания ID


@pytest.mark.run(order=4)
def test_update_project_invalid_id_negative():
    update_payload = {'title': 'Обновленный проект'}
    project_api.check_update_project_invalid_id('invalid_id', update_payload)


@pytest.mark.run(order=4)
def test_update_project_nonexistent_id_negative():
    update_payload = {'title': 'Обновленный проект'}
    project_api.check_update_project_nonexistent_id(
        '4f6f3091-0f94-4d30-9b0e-99430a36d4fb', update_payload
    )


if __name__ == '__main__':
    pytest.main()
