# Gerador de relatório de custos para implantação de placas solares

## Instalação
- Clone o repositório

```bash
git clone https://github.com/devwenderson gerador-de-relatorio-placa-solar.git
```
- Crie um ambiente virtual

```bash
py -m venv .venv
```

- Ative o ambiente virtual

_windows_
```powershell
.venv/Scripts/activate
```
_linux, macOs_
```bash
source .venv/bin/activate
```

---
### Configurando sua máquina

- Instale as dependências

```bash
pip install -r requirements.txt
```

- Crie as variáveis de ambiente

```bash
python scripts/env_gen.py
```

- Altere os dados do aquivo `.env`
```env
DEFAULT_FROM_EMAIL = '<seu email>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = '<seu email>'
EMAIL_HOST_PASSWORD = '<senha de app>'
```
> A senha de app NÃO pode conter espaçamento entre os caracteres. Para criar uma, acesse o link abaixo :point_down:

> [Como gerar senha de app aqui](https://www.youtube.com/watch?v=nFbZLX2U-5k&pp=ygUgY29tbyBnZXJhciBzZW5oYSBkZSBhcHAgbm8gZ21haWw%3D)


