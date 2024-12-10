
    // Function initializes pkg_map correctly when valid inputs are provided
void test_initialize_pkg_map_valid_inputs() {
    int num_nodes = 4;
    int *pkg_map;
    APIC_ID_t os_map[4] = {
        {0, 0, 0},
        {1, 0, 0},
        {2, 0, 0},
        {3, 0, 0}
    };
    long os_cpu_count = 4;

    int result = initialize_pkg_map(num_nodes, pkg_map, os_map, os_cpu_count);

    assert(result == 0);
    for (int i = 0; i < num_nodes; i++) {
        assert(pkg_map[i] == i);
    }

    free(pkg_map);
}

    // Function handles NULL os_map gracefully
void test_initialize_pkg_map_null_os_map() {
    int num_nodes = 4;
    int *pkg_map;
    // known CVE
    APIC_ID_t *os_map = NULL;
    long os_cpu_count = 4;

    int result = initialize_pkg_map(num_nodes, pkg_map, os_map, os_cpu_count);

    assert(result == -1);
}
