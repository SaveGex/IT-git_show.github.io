import requests

def get_direct_image_link(github_link: str) -> str:
    if "github.com" in github_link:
        # Check if it's a general repo link
        if "/blob/" not in github_link:
            # Try to fetch the list of files from the repository
            api_url = github_link.replace("github.com", "api.github.com/repos")
            api_url += "/contents"  # GitHub API for listing files
            
            response = requests.get(api_url)
            if response.status_code == 200:
                files = response.json()
                # Look for an image file in the repository
                for file in files:
                    if file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        # Build the raw content link for the image
                        raw_link = file['download_url']
                        return raw_link
            return "No image found"
        else:
            # Handle direct links with 'blob'
            parts = github_link.split('/')
            username = parts[3]
            repo = parts[4]
            branch = parts[6]
            path_to_file = '/'.join(parts[7:])
            direct_link = f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/{path_to_file}"
            return direct_link
    else:
        return "Invalid GitHub link"
import requests

def get_github_profile_image(github_repo_link: str) -> str:
    if "github.com" in github_repo_link:
        parts = github_repo_link.split('/')
        if len(parts) >= 4:
            username = parts[3]
            # Запрос к GitHub API для получения данных пользователя
            api_url = f"https://api.github.com/users/{username}"
            response = requests.get(api_url)
            if response.status_code == 200:
                user_data = response.json()
                return user_data.get("avatar_url", "")
    return ""
