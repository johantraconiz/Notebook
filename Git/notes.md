# Git

## Ver el autor de los commits de un repo

```bash
git log --pretty=format:"%h %an <%ae> %ad" --date=short
```

## Ver con que correo se va a commitear el commit en el repo actual

```bash
git config user.email
```

## Gestionar multiples cuentas de git

En la raiz de la compu en johantraconiz, crear los siguientes archivos:

Nota: Esta es la forma correcta de configurar Git, ya no es necesario usar la extensión de VS Code llamada "git-autoconfig" la cual lo gestiona muy basico.

### .gitconfig

```text
# 🔐 Configuración global
[credential "https://*.*.sourcemanager.dev"]
    helper = gcloud.sh

# 👤 Configuración para la cuenta personal
[includeIf "gitdir:~/workspace/**"]
    path = ~/.gitconfig-personal

# 👨‍💻 Configuración para la cuenta de aida
[includeIf "gitdir:~/aida/**"]
    path = ~/.gitconfig-aida
```

### .gitconfig-aida

```text
[user]
    name = Johan Traconiz
    email = johan.bautista@soyaida.com
```

### .gitconfig-personal

```text
[user]
    name = Johan Traconiz
    email = johan.traconiz@gmail.com
```

## Actualizar origen del repo para vincular la autenticación

```bash
git remote set-url origin git@github-aida:aida-src/aida-service-conversations.git
```

```bash
git remote set-url origin git@github-aida:aida-src/aida-utils-commons.git
```

Nota:

* Atención en @github-aida esto es el Hostname configurado en ~/.ssh/config de SSH.
* Lo que sigue despues de los ":" es el path de clone con SSH que se obtiene del repo en github o gitlab en el boton de code que permite clonar el repo.

## Nombrar ramas

* Nueva funcionalidad → feat/
* Bug → fix/ o hotfix/
* Cambio visual (CSS, imágenes) → style/
* Documentación → docs/
* Optimización de rendimiento → perf/
* Refactorización → refactor/
* Tareas de mantenimiento → chore/
* Tests → test/

| **Prefijo**         | **Cuándo usarlo**                                                                                     | **Ejemplo**                        |
| ------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **feat/** (feature) | Para **nuevas funcionalidades** o grandes cambios.                                                    | `feat/add-dark-mode`               |
| **fix/**            | Para **corrección de bugs**.                                                                          | `fix/login-crash-on-ios`           |
| **hotfix/**         | Igual que `fix`, pero para **bugs críticos en producción**.                                           | `hotfix/payment-gateway-timeout`   |
| **chore/**          | Para **tareas de mantenimiento**, sin afectar la lógica. Ej: dependencias, build, renombrar archivos. | `chore/update-npm-packages`        |
| **style/**          | Para **cambios visuales** o de formato, sin modificar lógica (CSS, imágenes, alineaciones).           | `style/update-hero-banner`         |
| **refactor/**       | Para **reorganizar o mejorar código** sin cambiar funcionalidad.                                      | `refactor/simplify-auth-service`   |
| **perf/**           | Para **mejoras de rendimiento**.                                                                      | `perf/optimize-image-loading`      |
| **test/**           | Para **añadir o modificar tests**.                                                                    | `test/add-user-service-unit-tests` |
| **docs/**           | Para **documentación** o cambios en el README.                                                        | `docs/add-api-usage-guide`         |
| **build/**          | Para **cambios en la configuración de build**, CI/CD, Docker, etc.                                    | `build/update-dockerfile`          |
| **ci/**             | Para scripts o configuraciones de **integración continua**.                                           | `ci/fix-github-actions-pipeline`   |
| **revert/**         | Para **revertir un cambio anterior**.                                                                 | `revert/revert-user-auth-update`   |

## Contribuir a un repo

* git checkout dev
* git pull
* ⁠git checkout mi-branch
* ⁠git merge dev
