#!/bin/bash
clear

echo "[*] Verificando cambios en archivos de recursos y UI..."
path="$(dirname "$0")"

if ! git diff --quiet assets/resources.qrc; then
    echo "[+] Cambios en recursos, compilando..."
    pyside6-rcc assets/resources.qrc -o resources_rc.py
fi

cd "$path/ui" || exit

if ! git diff --quiet main_window.ui; then
    echo "[+] Cambios en main_window.ui, compilando..."
    pyside6-uic main_window.ui -o main_window.py
fi

if ! git diff --quiet about_us.ui; then
    echo "[+] Cambios en about_us.ui, compilando..."
    pyside6-uic about_us.ui -o about_us.py
fi

if ! git diff --quiet score.ui; then
    echo "[+] Cambios en score.ui, compilando..."
    pyside6-uic score.ui -o score.py
fi

