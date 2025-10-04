from ._commands import Commands
from ._comm import Arguments, Types, communicate

# TODO: parse outputs better

def job_scheduler_cancel_all() -> bytes:
    """Cancel all scheduled jobs"""
    out, err = communicate(Commands.job_scheduler, {Types.boolean: ("cancel_all", "true")})
    if err: raise Exception(err.decode())
    return out

def job_scheduler_pending() -> bytes:
    """Gets all pending jobs"""
    out, err = communicate(Commands.job_scheduler, {Types.boolean: ("pending", "true")})
    if err: raise Exception(err.decode())
    return out

def job_scheduler_cancel(job_id: int) -> bytes:
    """Cancel a scheduled job"""
    args = Arguments()
    args += (Types.boolean, "cancel", "true")
    args += (Types.integer, "job_id", str(job_id))
    out, err = communicate(Commands.job_scheduler, {Types.boolean: ("cancel_all", "true")})
    if err: raise Exception(err.decode())
    return out

def job_schedule(script_path: str, battery_not_low: bool = False, persisted: bool = False, storage_not_low: bool = False, charging: bool = False, period_ms: int = None, trigger_content_uri: str = "", trigger_content_flag: bool = False, network: str = None, job_id: int = None) -> bytes:
    """Schedule a job
    Args:
        script_path: str
        battery_not_low: str
        persisted: bool
        storage_not_low: bool
        charging: bool
        period_ms: bool
        trigger_content_uri: str
        trigger_content_flag: bool
        network: str
        job_id: int"""
    args = Arguments()
    args += (Types.string, "script", script_path)
    if job_id: args += (Types.string, "job_id", str(job_id))
    if battery_not_low: args += (Types.boolean, "battery_not_low", "true")
    if persisted: args += (Types.boolean, "persisted", "true")
    if storage_not_low: args += (Types.boolean, "storage_not_low", "true")
    if period_ms: args += (Types.integer, "period_ms", str(period_ms))
    if trigger_content_uri: args += (Types.string, "trigger_content_uri", str(trigger_content_uri))
    if trigger_content_flag: args += (Types.boolean, "trigger_content_flag", "true")
    if network: args += (Types.string, "network", "true")
    out, err = communicate(Commands.job_scheduler, args)
    if err: raise Exception(err.decode())
    return out
