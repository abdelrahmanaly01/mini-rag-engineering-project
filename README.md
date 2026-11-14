# mini-rag

This project is for building a mini Retrieval-Augmented Generation (RAG) application. The goal is to retrieve relevant information from documents and use it to help a language model generate answers.

## Requirements

- **Python 3.10 or later**.
- **Miniconda** to create an isolated Python environment.
- For Windows users who want to work in Linux: **WSL 2 with Ubuntu**.

The repository is at an initial stage. Follow the setup steps below to install the current dependencies and create your local environment configuration.

## Set up Miniconda

### Windows

1. Download the Windows installer from the [official Miniconda installation guide](https://www.anaconda.com/docs/getting-started/installation).
2. Run the installer and follow the prompts.
3. Open **Anaconda Prompt (Miniconda)** and create the project environment:

   ```bat
   conda create --name mini-rag python=3.10 pip
   conda activate mini-rag
   python --version
   cd /d C:\myFiles\github\mini-rag
   ```

Python 3.10 is used as the baseline in these examples; you can choose a later Python version. Activate the environment with `conda activate mini-rag` whenever you start a new terminal session.

### Linux (including Ubuntu in WSL)

Run these commands in a Linux terminal. For Windows, first complete the WSL installation below, then return to this section from your Ubuntu terminal.

1. Install the download tools:

   ```bash
   sudo apt update
   sudo apt install -y curl ca-certificates
   ```

   These package commands are for Ubuntu and Debian-based distributions.

2. Check your architecture:

   ```bash
   uname -m
   ```

3. Download the matching Miniconda installer. For `x86_64`:

   ```bash
   curl -fLO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

   For `aarch64` (ARM64), use `Miniconda3-latest-Linux-aarch64.sh` in both commands instead.

4. Follow the installer prompts, accept the license if you agree, keep the default installation directory (`~/miniconda3`), and answer **yes** when asked to initialize conda. Close and reopen the Linux terminal afterward.

   If you skipped initialization, run:

   ```bash
   ~/miniconda3/bin/conda init bash
   source ~/.bashrc
   ```

5. Create and activate the environment:

   ```bash
   conda create --name mini-rag python=3.10 pip
   conda activate mini-rag
   python --version
   ```

   Confirm that Python reports version **3.10 or later**.

## Set up WSL Linux on Windows

1. On Windows 11 or Windows 10 version 2004 (build 19041) or later, open **PowerShell as Administrator** and run:

   ```powershell
   wsl --install -d Ubuntu
   ```

2. Restart Windows if prompted. Open **Ubuntu** from the Start menu and create your Linux username and password when prompted.

3. In PowerShell, check that Ubuntu uses WSL 2:

   ```powershell
   wsl --list --verbose
   ```

   If Ubuntu shows version 1, convert it:

   ```powershell
   wsl --set-version Ubuntu 2
   ```

4. In the Ubuntu terminal, follow the **Linux (including Ubuntu in WSL)** Miniconda steps above. Install Miniconda inside Ubuntu so the project uses a Linux Python environment.

## Work on the project from WSL

Open Ubuntu from the Start menu, or run `wsl -d Ubuntu` from PowerShell. In the Ubuntu terminal:

```bash
cd /mnt/c/myFiles/github/mini-rag
conda activate mini-rag
python --version
python -c "import sys; print(sys.executable)"
```

Windows drives are available under `/mnt` in WSL, so `C:\myFiles\github\mini-rag` becomes `/mnt/c/myFiles/github/mini-rag`. The Python executable should point to your Linux conda environment, typically under `~/miniconda3/envs/mini-rag/`.

Use this terminal and activated environment for dependency installation and application commands.

## Install dependencies and create `.env`

Run these commands from the repository root with the `mini-rag` Conda environment activated. Repeat the activation step whenever you open a new terminal.

### Windows

In **Anaconda Prompt (Miniconda)**:

```bat
cd /d C:\myFiles\github\mini-rag
conda activate mini-rag
python -m pip install -r requirements.txt
copy .env.example .env
```

### Linux (including Ubuntu in WSL)

In your Linux terminal:

```bash
conda activate mini-rag
python -m pip install -r requirements.txt
cp .env.example .env
```

If you are using WSL, first change to the project directory with `cd /mnt/c/myFiles/github/mini-rag`.

The `.env` file contains the local `APP_NAME` and `APP_VERSION` settings. Edit it if needed; it is ignored by Git. The committed `.env.example` provides the defaults for creating your local file.

When finished, leave the environment with:

```bash
conda deactivate
```

## Start Fest API server

From the repository root with the `mini-rag` environment activated, run:

```bash
uvicorn main:app --reload --host 0.0.0.0
```

## Setup references

- [Miniconda installation guide](https://www.anaconda.com/docs/getting-started/installation)
- [Conda installation documentation](https://docs.conda.io/projects/conda/en/stable/user-guide/install/)
- [Microsoft WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install)
