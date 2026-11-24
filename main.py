from modelfactory.pipeline import Pipeline


def main():
    Pipeline.from_yaml("configs/config.yaml").run()


if __name__ == "__main__":
    main()
