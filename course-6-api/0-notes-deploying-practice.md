- You should always breakdown your project into smaller aplications rather than having 1 application that does many features --> this avoids difficult debugging as well as difficult upgrade or adding new features.

- You should always avoid using global environments, and adhere to virtual environments for every app due to different dependendacies requirements and in some cases different versions.

- Use the following command to save all the dependencies into a text file.

```bash
pip3 freeze > requirements.txt
```

- If youre using `pipenv` it uses Piplock files to keep track of the dependencies -- when setting up your project for the first time, it takes the requiremnets from the requirements.txt file

- Have sepearte resources folders for each applicaitons

## Instead of placing all the logic into views, plcae them into Models , which makes it:

- powerful
- decoupled
- reusable
- less code

# In conclusion:

- Split App
- Use virtual environment
- Create new versions when updating app or its api
- List out all the dependencies
- Sepearte resource for each applications
- Multiple setting files
- Have business logic in the models rather than views
