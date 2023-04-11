# comiczip
a post process script for [smartstitch](https://github.com/mechtechnology/smartstitch).


### download
check out [releases](https://github.com/BishrGhalil/comiczip/releases) for executable file.


### build from source
**Requirements**:
- python
- pipenv

clone the repo and open the directory in the terminal emulator, Then:
```
pipenv install --dev
pipenv shell
pipenv run build
```

binary file will be located at the `dist` directory.

### usage
1. in smartstich, navigate to the `post process` tab
2. enable the run `post process after completion` flag
3. set the comiczip binary path/location, you can essentially browse to `comiczip.exe` file
4. add this `-i [stitched] -o [processed]` to the `post process arguments` field

![image](https://user-images.githubusercontent.com/75081255/231022920-e2ee958c-e142-4fdc-a08b-d12f907dbc74.png)
