# src/core/auth_provider.py
#
# Auth state provider for routingApp.
# Note: AuthService integration is deferred until backend setup.
#

import flet as ft
from typing import Optional
from config import logger
from models.userModel import UserProfile
from core.auth_context import AuthContext
from models.auth_context_model import AuthContextModel


def build_auth_state() -> AuthContextModel:
    """
    Build auth state hooks and return the AuthContextModel instance.
    Must be called from inside a @ft.component function.
    """
    # ─── State ──────────────────────────────────────────────────────────────
    user, set_user = ft.use_state(None)
    is_loading, set_is_loading = ft.use_state(False)
    error, set_error = ft.use_state(None)

    # ─── Action handlers (Placeholder until backend connection) ──────────────
    def handle_login(username: str, password: str) -> bool:
        logger.info(f"Login attempt for '{username}' (Backend connection pending)")
        return False

    def handle_logout() -> None:
        set_user(None)
        set_error(None)
        set_is_loading(False)
        logger.info("User logged out")
        try:
            ft.context.page.navigate("/")
        except Exception as e:
            logger.error(f"Logout navigation error: {e}")

    def handle_clear_error() -> None:
        set_error(None)

    # ─── Stable callbacks ───────────────────────────────────────────────────
    login_cb = ft.use_callback(handle_login, [user, is_loading, error])
    logout_cb = ft.use_callback(handle_logout, [user])
    clear_cb = ft.use_callback(handle_clear_error, [error])

    # ─── Context value ──────────────────────────────────────────────────────
    auth_value = ft.use_memo(
        lambda: AuthContextModel(
            user=user,
            is_authenticated=user is not None,
            is_loading=is_loading,
            error=error,
            login=login_cb,
            logout=logout_cb,
            clear_error=clear_cb,
        ),
        [user, is_loading, error, login_cb, logout_cb, clear_cb]
    )

    return auth_value