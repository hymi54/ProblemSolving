v_t, v_f, v_s, v_p, v_c = map(int, input().split())
h_t, h_f, h_s, h_p, h_c = map(int, input().split())

print(v_t*6 + v_f*3 + v_s*2 + v_p + v_c*2, h_t*6 + h_f*3 + h_s*2 + h_p + h_c*2)
