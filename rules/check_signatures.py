def check_signatures(flow_key, flow_stats, rule):
    # flow_key = (src_ip, dst_ip, src_port, dst_port, proto)
    # flow_stats = { 'packet_count': ..., 'byte_count': ..., ... }
    
    # 1) Protokol eşleşmesi
    if rule.get("proto") is not None:
        if flow_key[4] != rule["proto"]:
            return False
    
    # 2) Port eşleşmesi
    if rule.get("dst_port") is not None:
        if flow_key[3] != rule["dst_port"]:
            return False
    
    # 3) max_packet_count + time_window
    if rule.get("max_packet_count") and rule.get("time_window"):
        # flow_stats['first_time'], flow_stats['packet_count']
        if (time.time() - flow_stats['first_time']) < rule["time_window"]:
            if flow_stats['packet_count'] > rule["max_packet_count"]:
                return True
        return False
    
    # 4) TCP flags vs. Tek tek paket bazında incelemek gerekebilir
    # Bu, flow bazlı tabloda zor. Genelde her paket callback'inde flags kontrol edilir.
    
    # Varsayılan: Eşleşti sayalım
    return True
