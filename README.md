# custom-achievements-server

Readmes are overrated, at least if you know how the program works.

## Install

### Manual

#### Linux

Install:

```bash
$ sh setup.sh
```

Run:
```bash
$ sh run.sh
```

#### Windows

Install:

```bash
$ setup
```

Run:
```bash
$ run
```

### Docker

Download with:

```bash
$ docker pull jojojux/custom-achievements-server
```

Install with:

```bash
$ docker run -d -p 8055:8055 --name achievement-server jojojux/custom-achievements-server
```

Stop with:

```bash
$ docker stop achievement-server
```

Start with:

```bash
$ docker start achievement-server
```

Restart with:

```bash
$ docker achievement-server
```