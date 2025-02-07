import requests


class ProjectAPI:
    BASE_URL = 'https://ru.yougile.com/api-v2'

    def __init__(self, token):
        self.token = token
        self.project_ids = []

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    # POST Методы
    def create_project(self, payload):
        url = f"{self.BASE_URL}/projects"
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response

    def check_response(self, response, expected_status_code, key=None):
        assert response.status_code == expected_status_code
        if key:
            assert key in response.json()

    def extract_project_id(self, response):
        self.check_response(response, 201, 'id')
        project_id = response.json().get('id')
        self.project_ids.append(project_id)
        return project_id

    def create_project_with_role(self, role, user_id):
        payload = {
            'title': 'Проект 1',
            'users': {user_id: role}
        }
        response = self.create_project(payload)
        print(f"Response status: {response.status_code}, response content: {response.json()}")
        self.extract_project_id(response)

    def create_project_with_roles(self, user_id, roles):
        for role in roles:
            self.create_project_with_role(role, user_id)

    def create_project_with_new_user(self, new_user_id):
        payload = {
            'title': 'Проект 1',
            'users': {new_user_id: 'worker'}
        }
        response = self.create_project(payload)
        self.extract_project_id(response)

    def create_project_with_invalid_user_id(self, invalid_user_id):
        payload = {
            'title': 'Проект 1',
            'users': {invalid_user_id: 'worker'}
        }
        response = self.create_project(payload)
        self.check_response(response, 400, 'message')

    def create_project_without_title(self, user_id):
        payload = {
            'title': '',
            'users': {user_id: 'worker'}
        }
        response = self.create_project(payload)
        self.check_response(response, 400, 'message')

    def create_project_without_role(self, user_id):
        payload = {
            'title': 'Проект 1',
            'users': {user_id: ''}
        }
        response = self.create_project(payload)
        self.check_response(response, 400, 'message')

    def create_project_with_invalid_json(self, user_id):
        payload = {
            'titl': 'Проект 1',
            'user': {user_id: 'worker'}
        }
        response = self.create_project(payload)
        self.check_response(response, 400, 'message')

    # GET Методы
    def get_projects(self, params=None):
        url = f"{self.BASE_URL}/projects"
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response

    def check_get_projects(self):
        response = self.get_projects()
        self.check_response(response, 200)
        project_ids_from_response = [
            project['id'] for project in response.json()['content']
        ]
        assert all(
            project_id in project_ids_from_response
            for project_id in self.project_ids
        )

    def check_get_projects_with_title(self, title):
        params = {'title': title}
        response = self.get_projects(params=params)
        self.check_response(response, 200)

    def check_get_projects_with_limit(self, limit):
        params = {'limit': limit}
        response = self.get_projects(params=params)
        self.check_response(response, 200)

    def check_get_projects_with_offset(self, offset):
        params = {'offset': offset}
        response = self.get_projects(params=params)
        self.check_response(response, 200)

    # ID GET Методы
    def get_project_by_id(self, project_id):
        url = f"{self.BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=self.get_headers())
        return response

    def check_get_project_by_id(self, project_id):
        response = self.get_project_by_id(project_id)
        project_json = response.json()
        self.check_response(response, 200)
        assert 'title' in project_json
        assert 'id' in project_json
        assert 'timestamp' in project_json
        assert 'users' in project_json

    def check_get_project_by_invalid_id(self, invalid_project_id):
        response = self.get_project_by_id(invalid_project_id)
        project_json = response.json()
        self.check_response(response, 404)
        assert 'error' in project_json

    def check_get_project_by_nonexistent_id(self, nonexistent_project_id):
        response = self.get_project_by_id(nonexistent_project_id)
        project_json = response.json()
        self.check_response(response, 404)
        assert 'error' in project_json

    def get_and_check_first_project(self):
        response = self.get_projects()
        self.check_response(response, 200)
        project_ids = [project['id'] for project in response.json()['content']]
        assert len(project_ids) > 0, "No project IDs found"
        self.project_ids.extend(project_ids)  # Добавляем найденные ID проектов в список
        self.check_get_project_by_id(project_ids[0])

    # PUT Методы

    def update_project(self, project_id, payload):
        url = f"{self.BASE_URL}/projects/{project_id}"
        response = requests.put(url, json=payload, headers=self.get_headers())
        return response

    def check_update_project(self, project_id=None, update_payload=None):
        if project_id is None:
            if len(self.project_ids) > 0:
                project_id = self.project_ids[-1]  # Используем последний созданный проект
            else:
                raise ValueError("Список project_ids пуст. Невозможно обновить проект без ID.")

        if update_payload is None:
            update_payload = {}

        response = self.update_project(project_id, update_payload)
        json_response = response.json()
        self.check_response(response, 200)
        assert 'id' in json_response, (
            f"Key 'id' not found in response: {json_response}"
        )
        assert json_response['id'] == project_id

    def check_update_project_invalid_id(
            self, invalid_project_id, update_payload
            ):
        response = self.update_project(invalid_project_id, update_payload)
        json_response = response.json()
        self.check_response(response, 404)
        assert 'error' in json_response

    def check_update_project_nonexistent_id(
            self, nonexistent_project_id, update_payload
            ):
        response = self.update_project(nonexistent_project_id, update_payload)
        json_response = response.json()
        self.check_response(response, 404)
        assert 'error' in json_response
