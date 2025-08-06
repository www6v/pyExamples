# https://github.com/BerriAI/litellm/blob/main/litellm/proxy/proxy_server.py

from fastapi import (
    Depends,
    FastAPI,
    File,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    UploadFile,
    applications,
    status,
)

from contextlib import asynccontextmanager

from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware

import uvicorn


async def proxy_shutdown_event():
    global prisma_client, master_key, user_custom_auth, user_custom_key_generate
    # verbose_proxy_logger.info("Shutting down LiteLLM Proxy Server")
    # if prisma_client:
    #     verbose_proxy_logger.debug("Disconnecting from Prisma")
    #     await prisma_client.disconnect()

    # if litellm.cache is not None:
    #     await litellm.cache.disconnect()

    # await jwt_handler.close()

    # if db_writer_client is not None:
    #     await db_writer_client.close()

    # # flush remaining langfuse logs
    # if "langfuse" in litellm.success_callback:
    #     try:
    #         # flush langfuse logs on shutdow
    #         from litellm.utils import langFuseLogger

    #         if langFuseLogger is not None:
    #             langFuseLogger.Langfuse.flush()
    #     except Exception:
    #         # [DO NOT BLOCK shutdown events for this]
    #         pass

    ## RESET CUSTOM VARIABLES ##
    # cleanup_router_config_variables()

@asynccontextmanager
async def proxy_startup_event(app: FastAPI):
    global prisma_client, master_key, use_background_health_checks, llm_router, llm_model_list, general_settings, proxy_budget_rescheduler_min_time, proxy_budget_rescheduler_max_time, litellm_proxy_admin_name, db_writer_client, store_model_in_db, premium_user, _license_check, proxy_batch_polling_interval
    import json

    # init_verbose_loggers()
    # ## CHECK PREMIUM USER
    # verbose_proxy_logger.debug(
    #     "litellm.proxy.proxy_server.py::startup() - CHECKING PREMIUM USER - {}".format(
    #         premium_user
    #     )
    # )
    # if premium_user is False:
    #     premium_user = _license_check.is_premium()

    # ## CHECK MASTER KEY IN ENVIRONMENT ##
    # master_key = get_secret_str("LITELLM_MASTER_KEY")
    # ### LOAD CONFIG ###
    # worker_config: Optional[Union[str, dict]] = get_secret("WORKER_CONFIG")  # type: ignore
    # env_config_yaml: Optional[str] = get_secret_str("CONFIG_FILE_PATH")
    # verbose_proxy_logger.debug("worker_config: %s", worker_config)
    # # check if it's a valid file path
    # if env_config_yaml is not None:
    #     if os.path.isfile(env_config_yaml) and proxy_config.is_yaml(
    #         config_file_path=env_config_yaml
    #     ):
    #         (
    #             llm_router,
    #             llm_model_list,
    #             general_settings,
    #         ) = await proxy_config.load_config(
    #             router=llm_router, config_file_path=env_config_yaml
    #         )
    # elif worker_config is not None:
    #     if (
    #         isinstance(worker_config, str)
    #         and os.path.isfile(worker_config)
    #         and proxy_config.is_yaml(config_file_path=worker_config)
    #     ):
    #         (
    #             llm_router,
    #             llm_model_list,
    #             general_settings,
    #         ) = await proxy_config.load_config(
    #             router=llm_router, config_file_path=worker_config
    #         )
    #     elif os.environ.get("LITELLM_CONFIG_BUCKET_NAME") is not None and isinstance(
    #         worker_config, str
    #     ):
    #         (
    #             llm_router,
    #             llm_model_list,
    #             general_settings,
    #         ) = await proxy_config.load_config(
    #             router=llm_router, config_file_path=worker_config
    #         )
    #     elif isinstance(worker_config, dict):
    #         await initialize(**worker_config)
    #     else:
    #         # if not, assume it's a json string
    #         worker_config = json.loads(worker_config)
    #         if isinstance(worker_config, dict):
    #             await initialize(**worker_config)

    # # check if DATABASE_URL in environment - load from there
    # if prisma_client is None:
    #     _db_url: Optional[str] = get_secret("DATABASE_URL", None)  # type: ignore
    #     prisma_client = await ProxyStartupEvent._setup_prisma_client(
    #         database_url=_db_url,
    #         proxy_logging_obj=proxy_logging_obj,
    #         user_api_key_cache=user_api_key_cache,
    #     )

    # ProxyStartupEvent._initialize_startup_logging(
    #     llm_router=llm_router,
    #     proxy_logging_obj=proxy_logging_obj,
    #     redis_usage_cache=redis_usage_cache,
    # )

    # ## JWT AUTH ##
    # ProxyStartupEvent._initialize_jwt_auth(
    #     general_settings=general_settings,
    #     prisma_client=prisma_client,
    #     user_api_key_cache=user_api_key_cache,
    # )

    # if use_background_health_checks:
    #     asyncio.create_task(
    #         _run_background_health_check()
    #     )  # start the background health check coroutine.

    # if prompt_injection_detection_obj is not None:  # [TODO] - REFACTOR THIS
    #     prompt_injection_detection_obj.update_environment(router=llm_router)

    # verbose_proxy_logger.debug("prisma_client: %s", prisma_client)
    # if prisma_client is not None and litellm.max_budget > 0:
    #     ProxyStartupEvent._add_proxy_budget_to_db(
    #         litellm_proxy_budget_name=litellm_proxy_admin_name
    #     )

    # ### START BATCH WRITING DB + CHECKING NEW MODELS###
    # if prisma_client is not None:
    #     await ProxyStartupEvent.initialize_scheduled_background_jobs(
    #         general_settings=general_settings,
    #         prisma_client=prisma_client,
    #         proxy_budget_rescheduler_min_time=proxy_budget_rescheduler_min_time,
    #         proxy_budget_rescheduler_max_time=proxy_budget_rescheduler_max_time,
    #         proxy_batch_write_at=proxy_batch_write_at,
    #         proxy_logging_obj=proxy_logging_obj,
    #     )

    #     await ProxyStartupEvent._update_default_team_member_budget()

    # ## [Optional] Initialize dd tracer
    # ProxyStartupEvent._init_dd_tracer()

    # End of startup event
    yield

    # Shutdown event
    await proxy_shutdown_event()

app = FastAPI(
    docs_url="",
    redoc_url="",
    title="My API",
    description="",
    version="2.1.0",
    root_path="",  # check if user passed root path, FastAPI defaults this value to ""
    lifespan=proxy_startup_event,
)


router = APIRouter()
origins = ["*"]


app.mount("/", router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get(
    "/v1/models/{model_id}",
    # dependencies=[Depends(user_api_key_auth)],
    tags=["model management"],
)
@router.get(
    "/models/{model_id}",
    # dependencies=[Depends(user_api_key_auth)],
    tags=["model management"],
)
async def model_info(
    model_id: str,
    # user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),
):
    # """
    # Retrieve information about a specific model accessible to your API key.

    # Returns model details only if the model is available to your API key/team.
    # Returns 404 if the model doesn't exist or is not accessible.

    # Follows OpenAI API specification for individual model retrieval.
    # https://platform.openai.com/docs/api-reference/models/retrieve
    # """
    # global llm_model_list, general_settings, llm_router, prisma_client, user_api_key_cache, proxy_logging_obj

    # from litellm.proxy.utils import (
    #     create_model_info_response,
    #     get_available_models_for_user,
    #     validate_model_access,
    # )

    # # Get available models for the user
    # all_models = await get_available_models_for_user(
    #     user_api_key_dict=user_api_key_dict,
    #     llm_router=llm_router,
    #     general_settings=general_settings,
    #     user_model=user_model,
    #     prisma_client=prisma_client,
    #     proxy_logging_obj=proxy_logging_obj,
    #     team_id=None,
    #     include_model_access_groups=False,
    #     only_model_access_groups=False,
    #     return_wildcard_routes=False,
    #     user_api_key_cache=user_api_key_cache,
    # )

    # # Validate that the requested model is accessible
    # validate_model_access(model_id=model_id, available_models=all_models)

    # # Get provider information
    # _, provider, _, _ = litellm.get_llm_provider(model=model_id)

    # # Return the model information in the same format as the list endpoint
    # return create_model_info_response(
    #     model_id=model_id,
    #     provider=provider,
    #     include_metadata=False,
    #     fallback_type=None,
    #     llm_router=llm_router,
    # )

    return {"a": 1, "b": 2}



app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

