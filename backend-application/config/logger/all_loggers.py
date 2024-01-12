from .main import CustomLogger


users_logger = CustomLogger(logger_name='users',file_name="users_logger.log").get_logger()



def create_user_log_message(
    message = None,
    state = None,
    module = None 
):  
    if state == "warning":
        users_logger.warning(
            f"{module} | {message} "
        )
    elif state == "info":
        users_logger.info(
            f"{module} | {message} "
        )

    elif state == "error":
        users_logger.error(
            f"{module} | {message} "
        )

    elif state == "critical":
        users_logger.critical(
            f"{module} | {message} "
        )

    elif state == "debug":
        users_logger.debug(
            f"{module} | {message} "
        )
    