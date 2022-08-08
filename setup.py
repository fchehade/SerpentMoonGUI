from setuptools import setup, find_packages

setup(
    name='SerpentMoon',
    version='0.1.0',
    packages=find_packages(include=["SerpentMoonGUI", "SerpentMoonGUI.*"]),
    url='https://www.github.com/fchehade/SerpentMoonGUI',
    license='MIT',
    author='Fouzy Robert Chehade',
    author_email='fouzy_chehade@icloud.com',
    description='A tool to calculate the amount of needed event points per day in the Hunt: Showdown Serpent Moon Event',
    entry_points={"console_scripts": ["moon = SerpentMoonGUI.main:main"]},
    package_data={"": ["art/*"]},
    include_package_data=True
)
