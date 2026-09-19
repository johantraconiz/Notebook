# Configurar SSH Key

## Configura el archivo ~/.ssh/config

```ssh
# Cuenta personal: GitHub
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
  IdentitiesOnly yes

# Cuenta de trabajo: GitHub (Aida)
Host github-aida
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_aida
  IdentitiesOnly yes

# Cuenta de trabajo: GitLab (Aida)
Host gitlab-aida
  HostName gitlab.com
  User git
  IdentityFile ~/.ssh/id_ed25519_aida
  IdentitiesOnly yes
```

## Crear Keys

```bash
ssh-keygen -t ed25519 -C "tu_email_personal@example.com" -f ~/.ssh/id_ed25519_personal
```

```bash
ssh-keygen -t ed25519 -C "tu_email_laboral@example.com" -f ~/.ssh/id_ed25519_aida
```

## Agrega tus llaves al ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_aida
```

## Agrega la llave pública a cada plataforma

🔗 GitHub Personal
Ve a: <https://github.com/settings/keys>

Agrega la llave pública:

```bash
cat ~/.ssh/id_ed25519_personal.pub
```

Copiar todo hasta el coreeo de lo que muestra personal.pub y agregarlo a las SSH Keys de GitHub o GitLab según sea el caso.

## Clonar un repo

```bash
git clone git@github-personal:TU-USUARIO/REPO.git
```

Nota:

* Atención en @github-aida esto es el Hostname configurado en ~/.ssh/config de SSH.
* Lo que sigue despues de los ":" es el path de clone con SSH que se obtiene del repo en github o gitlab en el boton de code que permite clonar el repo.

## Verificar que todo funciona

```bash
ssh -T git@github-personal
```

resultado: Hi johantraconiz! You've successfully authenticated...

## Actualizar origen del repo para vincular la autenticación

```bash
git remote set-url origin git@github-aida:aida-src/aida-service-conversations.git
```

Nota:

* Atención en @github-aida esto es el Hostname configurado en ~/.ssh/config de SSH.
* Lo que sigue despues de los ":" es el path de clone con SSH que se obtiene del repo en github o gitlab en el boton de code que permite clonar el repo.
