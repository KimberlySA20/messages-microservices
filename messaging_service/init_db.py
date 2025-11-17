#!/usr/bin/env python3
"""
Script para inicializar la base de datos PostgreSQL en Azure
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from app.db import init_db, SessionLocal, Conversation, ConversationParticipant, Message
from seed import main as seed_main

def init_and_seed():
    """Crear tablas y cargar datos de prueba"""
    print("🔧 Creando tablas en PostgreSQL...")
    init_db()
    print("✅ Tablas creadas exitosamente")
    
    print("🌱 Cargando datos de prueba...")
    seed_main()
    print("✅ Datos de prueba cargados")

if __name__ == "__main__":
    init_and_seed()
