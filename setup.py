from setuptools import setup, find_packages

setup(
    name = 'insta-feed-checker',
    version = '1.0.0',
    description = "The fastest and simplest way to check someone's instagram feeds",
    long_description = open('README.md', encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    author = 'gibiee',
    author_email = 'gibiee@naver.com',
    url = 'https://github.com/gibiee/insta-feed-checker',
    download_url = '',
    packages = find_packages(exclude=[]),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['requests'],
    python_requires ='>=3.6',
    license = 'MIT',
    keywords = ['instagram', 'crawler', 'crawling', 'instagram_crawler', 'instagram_crawling', 'instacrawler'],
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)