import os
from flask import Flask, render_template
from sagra_downloader.page_scraper import SagraPageContent

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.sagreinemilia.it/sagre_per_provincia/8/ferrara"
    try:
        sagra_content = SagraPageContent(
            url=url
        )
        sagra_info = sagra_content.get_sagra_content()
    except Exception as exc:
        print(f"Impossible to get sagra information.")
        sagra_info = []

    return render_template(
        'index.html',
        sagra_info=sagra_info,
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)