type Reader struct {
  r    io.Reader
  pad  int64     
  curr fileReader
}
