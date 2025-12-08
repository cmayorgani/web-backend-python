USE FileDB;

INSERT INTO UploadedFiles (FileName, ParamA, ParamB)
VALUES ('demo.csv', 'paramA', 'paramB');

INSERT INTO CsvRows (FileId, RowNumber, Col1, Col2, Col3)
VALUES (1, 1, 'a', '1.2', 'x'),
       (1, 2, 'b', '2.3', 'y');
