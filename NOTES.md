# QDCG

`qdcg` - Python CLI for tool which the agent can call directly, exposes subcommands.

`core` - C++23 library for main graph data structure, indexing, and building snapshots.

`index` - C++23 binary for 1st indexing, either called by user or agent itself

`worker` - C++23 binary which owns the live graph for the duration of a session. Spawned by `qdcg`, loads snapshot, builds query engine, communicate with `qdcg` over stdin and stdout. Per query: runs freshness check, rebuilds the if stale, returns JSON. Kills itself if idle for more than 5 minutes _between_ requests.
