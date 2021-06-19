from dynaconf import Dynaconf

settings = Dynaconf(
    # all variables from settings.toml would be available as environment variables
    # with prefix `envvar_prefix`.
    # it means `some_var` would be `RECONGIZER_SOME_VAR`
    envvar_prefix="RECOGNIZER",
    # Note: there is .secrets.toml file that isn't available in the projects because
    # that is in gitignore file.
    settings_files=['settings.toml', '.secrets.toml'],
)
