require 'open-uri'

task 'assignment1' => 'assignment1.pdf'

task 'assignment3' => 'assignment3.pdf'

file 'apa.csl' do |t|
  open(t.name, 'w') do |f|
    f << open('https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl').read
  end
end

rule '.pdf' => '.md' do |t|
  sh "pandoc #{t.source} -o #{t.name}"
end

file 'assignment3.pdf' => ['assignment3.md', 'apa.csl'] do |t|
  sh "pandoc --filter pandoc-citeproc #{t.source} -o #{t.name}"
end
