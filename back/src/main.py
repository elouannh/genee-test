from envconfig import Development
import os
from dotenv import load_dotenv

from utils import create_app

load_dotenv()

match os.getenv('ENV'):
    case 'dev':
        config = Development()
    # Only the dev env
    case _:
        config = Development()

print(f"Using environment {config.ENV}")

app = create_app(config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
